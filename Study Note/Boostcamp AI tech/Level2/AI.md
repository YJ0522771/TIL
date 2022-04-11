# AI

* Grad CAM++의 원리

  * CAM

  * Grad-CAM

    CAM은 예측 직전에 GAP을 사용하는 특정 CNN 구조에만 적용 가능함. gradient를 feature map의 원소가 class 예측에 주는 영향으로 두어, CAM에서의 weight를 대신함.

  * Grad-CAM++

    Grad CAM은 같은 이미지 안에 같은 class의 여러 객체가 있을 경우 localization이 힘들다. Grad CAM에서 gradient의 단순 평균을 구했다면, Grad-CAM++에서는 단순 평균이 아닌 weighted sum을 사용.

  

* 활성화 함수 (Activation Function)란?

  입력신호의 총합을 출력신호로 변환하는 함수. 입력신호의 총합이 활성화를 일으키는지 결정.

  해당 신호를 다음으로 전달할지 여부를 결정.

  예시: 

  

* 과적합 (overfitting) 시 어떻게 해야하는가?

  1. 데이터의 양을 늘린다. (augmentation)

  2. 모델의 복잡도를 줄인다. (hidden layer, parameters)

  3. Regularization

     모델의 구조가 복잡해질수록 계수가 점점 커지고, 값의 작은 차이에도 민감하게 반응한다. 계수 크기에 상한선을 두어 일정 수준 이상 커지지 못하도록 한다.

     ex) L1 regularization, L2 regularization

  4. Dropout - 노드의 일부분을 랜덤하게 비활성화.

  5. Early Stopping - validation set으로 평가하여 overfitting이 되기 시작하면 멈춘다.



* 컨볼루션이란? (좀 더 조사)

  커널이라는 작은 matrix를 입력 데이터상에서 순차적으로 움직여가며 feature map을 연산하는 방법. 위치 정보를 유지하며 주변 pixel과의 관계를 고려할 수 있다.



* confusion matrics란?

  모델의 예측 성능을 표현. TP, TN, FP, FN으로 표현.

  1. TP (True Positive) : P를 P라고 예측.
  2. TN (True Negative) : N을 N이라고 예측.
  3. FP (False Positive) : N을 P라고 예측.
  4. FN (False Negative) : P를 N이라고 예측.



* 앙상블/보팅/배깅/부스팅 설명

  1. 앙상블

     더 나은 성능을 위해 여러 학습 모델을 결합하는 기법. 크게 보팅, 배깅, 부스팅이 있다.

  2. 보팅

     1. 하드 보팅

        여러 모델의 예측 결과값 중 다수를 차지하는 것을 선정.

     2. 소프트 보팅

        여러 모델의 예측 score 값의 평균을 구한 뒤, 가장 높은 score의 label을 선정.

  3. 배깅

     크기가 동일한 n개의 표본 데이터셋을 만들고, 각 데이터셋을 독립적으로 학습.

     일반적인 보팅 방식으로 결과를 합침.

  4. 부스팅

     앞선 모델의 학습 결과에서 오분류된 데이터들에 더 큰 가중치를 부여하여 학습하는 것을 반복.

     최종 결과 도출 시 가중치를 부여. 더 잘 학습된 모델에 높은 가중치 부여.

     배깅에 비해 성능은 좋지만, 느리고 과적합의 가능성이 상대적으로 높다.

     

* Augmentation이란?

  원본 데이터를 인위적으로 변화 시킴. 학습 데이터에 다양성을 주어 과적합을 막고 일반화가 잘 되도록 한다.

  간단하게 resize, flip, rotate, noise, blur 등이 자주 사용되고, cutout, mixup, cutmix, mosaic 등의 방법도 존재한다.

  test set과 비슷한 분포가 아니라면 효과가 없거나 오히려 성능이 떨어질 수도 있다. 



* batch norm이란?

  batch 단위로 학습 시, batch마다 분포가 달라 편향된 학습이 진행될 수 있다. 딥러닝에서 layer가 깊어질수록 weight 값의 변화에 민감하게 반응하므로, 이를 평균 0, 분산 1인 분포로 normalization 하여 보완. batch의 크기가 너무 작거나 클 경우에는 효과가 미미할 수 있다.



* sgd와 adam?

  * SGD

    train set 전체에 대해 loss를 계산하려면 계산량이 너무 많아지기 때문에 데이터 한 개 또는 일부 (batch)에 대해서만 loss를 계산. 전체를 계산하는 것보다 다소 부정확할 수는 있지만 반복을 통해 전체를 계산하는 것과 유사하게 수렴.

    데이터 한 개를 사용하는 경우 : Stochastic Gradient Descent(SGD)

    일부를 사용하는 경우 : mini-batch Stochastic Gradient Descent(mini-batch SGD)

  * Adam

    1. Adagrad : local minimum을 피하기 위해 과거 기울기 변화량을 고려하여 스텝의 크기를 결정. (momentum) 기울기 소실의 문제.
    2. RMSProp : 최근 기울기 변화량에 더 큰 가중치를 둔다.
    3. Adam : Adagrad와 RMSProp의 장점을 합침. 스텝 크기에 bounded norm 적용.



* transfer learning

  특정 분야에서 학습된 신경망의 일부를 유사하거나 전혀 새로운 분야에서 사용되는 신경망의 학습에 이용하는 것. 적은 학습으로 높은 성능을 기대할 수 있다.



* segmentation

  이미지에서 객체들을 의미 있는 단위로 분할하는 분야. 픽셀 단위로 label을 예측.

  sementic

  instance



* GAN

  생산적 적대 신경망 (Generative Adversarial Networks). 의미 있는 데이터를 생성하는 신경망.

  가짜 데이터를 생성하는 생성자 (Generator)와 생성자가 만들어낸 데이터와 진짜를 구별하는 판별자 (Descriminator)로 이루어져 있으며, 이 둘이 경쟁을 하며 학습하는 구조.



* object detection

  이미지에서 다수의 물체에 대해 class와 bounding box를 예측하는 분야.

  1-stage detector : classification과 localization을 동시에 수행. 속도가 빠르고 정확도가 상대적으로 낮음.

  2-state detector : 물체가 존재할만한 영역 (region proposal)을 먼저 찾고, classification을 진행. 속도는 느리지만 상대적으로 정확도가 높음.



* visualization (CAM)

  모델이 학습한 결과를 이해하기 쉽게 시각적으로 표현하는 것. 대표적으로 이미지 분류에서 모델이 어느 곳을 중점적으로 봤는 지를 시각화하는 CAM이 존재한다.



* 지도 학습/비지도 학습/준지도 학습

  1. 지도 학습

     학습 데이터의 정답이 주어지고, 이를 모델이 학습하는 방법. 정확도가 높다.

     분류 (classification), 회귀 (regression)

  2. 비지도 학습

     학습 데이터에 정답이 주어지지 않고 모델 스스로 데이터의 특성을 학습. 컨트롤이 힘들다.

     군집화 (Clustering), 시각화 (Visularization), 차원 축소 (Dimensionality Reduction)

  3. 준지도 학습

     정답이 존재하는 데이터와 존재하지 않는 데이터를 모두 학습에 사용. 더 많은 데이터를 확보할 수 있다. 하지만 정답이 없는 데이터에 대해서는 labeling이 불확실하다는 단점이 있다.



* one hot encoding 이란 무엇이고 적용해야하는 이유는?

  표현하고자 하는 대상의 전체 집합의 크기와 차원이 같은 벡터에 대해, 표현하고자 하는 것에는 1, 그 외에는 0 값을 주어 표현. classification 분야에서는 전체 클래스 수와 같은 차원의 백터에 해당되는 클래스에만 1의 값을 주어 label을 표현한다.



* GD란 무엇인가?

  현재 위치에서 함수의 기울기를 구하고, 기울기의 반대 방향으로 이동하며 극소값을 찾는 방법. loss 함수가 최소가 되는 weight 값을 찾기 위해 사용한다.

  임의의 초기 위치에서 기울기를 구하고, 기울기의 반대 방향으로 위치를 점점 이동해가며 극소값을 찾는다.



* GD의 문제점은?

  1. 데이터가 많아질수록 계산량 증가. → 학습 속도가 느려짐.

  2. local minimum

     활성화 함수로 인해 loss가 울퉁불퉁한 형태가 될 수 있으며, 이로 인해 local minimum에 수렴하여 진짜 최소값을 찾지 못 할 수가 있다.

  3. Plateau

     loss에 평탄한 구간이 있을 경우, 기울기의 크기에 따라 위치 이동 정도를 구하므로 학습 속도가 매우 느려짐.

  4. Zigzag

     여러 parameter에 대해, 각 값의 scale이 다를 경우 loss 함수의 변화에 미치는 영향이 달라진다. 이로 인해 학습 속도가 느려질 수 있다.



지원 직무 등 원하는 수식어를 넣어 임팩트 있게 시작.

단점은 굳이 말하지 말고, 강점만 강조. 자신감 있게.

경력, 경험, 수강 등을 어필.

장점 한 두가지 넣으면 좋음.

마지막에 꼭 뽑아달라는 느낌의 강조로 마무리 멘트.



비지도 학습에서 정답이 없는 데이터를 어떤 식으로 학습에 사용하는가

