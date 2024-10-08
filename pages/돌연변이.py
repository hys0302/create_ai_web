import random
import matplotlib
matplotlib.use('Agg')  # GUI 백엔드가 없는 환경에서 matplotlib 사용 설정
import matplotlib.pyplot as plt

def simulate_meiosis(normal=True):
    """
    감수 분열을 시뮬레이션하는 함수입니다.
    normal=True인 경우 정상적인 염색체 분리, False인 경우 비정상적인 염색체 분리를 시뮬레이션합니다.
    """
    parent_chromosomes = [1, 1, 2, 2]  # 상동 염색체 쌍 (2쌍)
    cell1, cell2 = [], []

    if normal:
        # 정상적인 분리: 각 세포에 상동 염색체 하나씩 분리됨
        random.shuffle(parent_chromosomes)
        cell1 = parent_chromosomes[:2]
        cell2 = parent_chromosomes[2:]
    else:
        # 비정상적인 분리: 염색체가 제대로 나누어지지 않음 (이수성 돌연변이 발생)
        random.shuffle(parent_chromosomes)
        cell1 = parent_chromosomes[:3]  # 한 세포에 염색체가 3개
        cell2 = parent_chromosomes[3:]  # 다른 세포에 염색체가 1개

    return cell1, cell2

def plot_results(normal_cell1, normal_cell2, abnormal_cell1, abnormal_cell2):
    """
    시뮬레이션 결과를 시각적으로 보여주는 함수입니다.
    """
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # 정상적인 감수 분열 결과 시각화
    axs[0].bar(['Cell 1', 'Cell 2'], [len(normal_cell1), len(normal_cell2)], color=['blue', 'green'])
    axs[0].set_title('정상적인 감수 분열')
    axs[0].set_ylabel('염색체 수')
    axs[0].set_ylim(0, 4)

    # 비정상적인 감수 분열 결과 시각화
    axs[1].bar(['Cell 1', 'Cell 2'], [len(abnormal_cell1), len(abnormal_cell2)], color=['red', 'orange'])
    axs[1].set_title('비정상적인 감수 분열 (이수성 돌연변이)')
    axs[1].set_ylabel('염색체 수')
    axs[1].set_ylim(0, 4)

    plt.tight_layout()
    plt.savefig('meiosis_simulation.png')  # 결과를 파일로 저장

def main():
    # 정상적인 감수 분열 시뮬레이션
    normal_cell1, normal_cell2 = simulate_meiosis(normal=True)

    # 비정상적인 감수 분열 시뮬레이션 (이수성 돌연변이)
    abnormal_cell1, abnormal_cell2 = simulate_meiosis(normal=False)

    # 결과 시각화
    plot_results(normal_cell1, normal_cell2, abnormal_cell1, abnormal_cell2)

if __name__ == "__main__":
    main()