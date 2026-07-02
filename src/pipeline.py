from skeleton_furniture.skeletonizer import Skeletonizer
from skeleton_furniture.edge_detector import EdgeDetector
from skeleton_furniture.contour_detector import ContourDetector

@dataclass
class Pipeline:
    image: np.ndarray

    def process(self) -> np.ndarray:
        # Apply the image processing pipeline to the input image
        skeletonizer = Skeletonizer(self.image)
        edges = EdgeDetector(skeletonizer.skeletonize()).detect_edges()
        contours = ContourDetector(edges).detect_contours()
        return contours