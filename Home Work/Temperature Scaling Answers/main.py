from scaling_diagrams import reliability_diagrams

logit_files = ["./sample_logits.p"]

reliability_diagrams(logit_files, plot_names=["Demo "], M=10)