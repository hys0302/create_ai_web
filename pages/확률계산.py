import random
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st

def simulate_offspring(parent1, parent2, num_simulations=1000):
    """
    부모 유전자형을 바탕으로 자손의 유전자형을 시뮬레이션하는 함수입니다.
    
    Parameters:
    parent1 (str): 부모1의 유전자형 (예: 'Rr')
    parent2 (str): 부모2의 유전자형 (예: 'Rr')
    num_simulations (int): 시뮬레이션 횟수
    
    Returns:
    dict: 자손 유전자형과 그 빈도를 포함한 딕셔너리
    """
    offspring_genotypes = []
    
    for _ in range(num_simulations):
        # 부모의 유전자를 각각 랜덤하게 선택
        allele1 = random.choice(parent1)
        allele2 = random.choice(parent2)
        # 자손의 유전자형을 정렬된 문자열로 생성 (예: 'Rr' 또는 'rR' -> 'Rr')
        offspring_genotypes.append(''.join(sorted(allele1 + allele2)))
    
    # 자손 유전자형 빈도 계산
    genotype_counts = Counter(offspring_genotypes)
    
    return genotype_counts

def plot_results(genotype_counts, num_simulations):
    """
    시뮬레이션 결과를 시각화하는 함수입니다.
    
    Parameters:
    genotype_counts (dict): 자손 유전자형과 그 빈도를 포함한 딕셔너리
    num_simulations (int): 시뮬레이션 횟수
    """
    genotypes = list(genotype_counts.keys())
    counts = list(genotype_counts.values())
    
    # 확률 계산
    probabilities = [count / num_simulations for count in counts]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(genotypes, probabilities, color=['blue', 'green', 'red'])
    ax.set_xlabel('Genotype')
    ax.set_ylabel('Probability')
    ax.set_title('Genotype Probability Simulation')
    ax.set_ylim(0, 1)
    for i, prob in enumerate(probabilities):
        ax.text(i, prob + 0.02, f'{prob:.2f}', ha='center')
    
    return fig

def main():
    st.title("유전자형 확률 시뮬레이션")
    st.write("이 프로그램은 부모의 유전자형을 바탕으로 자손의 유전자형이 나타날 확률을 시뮬레이션합니다.")
    
    # 부모 유전자형 입력
    parent1 = st.text_input("부모 1의 유전자형 (예: 'Rr')", 'Rr')
    parent2 = st.text_input("부모 2의 유전자형 (예: 'Rr')", 'Rr')
    num_simulations = st.slider("시뮬레이션 횟수", min_value=100, max_value=5000, value=1000)
    
    if st.button("시뮬레이션 실행"):
        # 시뮬레이션 실행
        genotype_counts = simulate_offspring(parent1, parent2, num_simulations)
        
        # 결과 출력
        st.write("자손의 유전자형 빈도:")
        for genotype, count in genotype_counts.items():
            st.write(f"{genotype}: {count} ({count / num_simulations:.2%})")
        
        # 결과 시각화
        fig = plot_results(genotype_counts, num_simulations)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
