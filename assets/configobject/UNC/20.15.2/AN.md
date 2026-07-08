---
id: UNC@20.15.2@ConfigObject@AN
type: ConfigObject
name: AN（复位AN）
nf: UNC
version: 20.15.2
object_name: AN
object_kind: action
applicable_nf:
- AMF
status: active
---

# AN（复位AN）

## 说明

![](复位AN（RST AN）_09653159.assets/notice_3.0-zh-cn_2.png)

该命令触发AMF发送到指定NG-RAN的RESET消息；当NG-RAN收到AMF的RESET消息后将立即释放UE的NG连接和UU连接资源，造成相关用户的业务中断。

**适用NF：AMF**

当AMF发生局部故障（比如个别业务进程异常）或者整体故障恢复后，会向NG-RAN发送RESET消息以同步UE的状态；NG-RAN收到AMF的RESET消息后，会释放指定用户的上下文（包括NG连接和UU连接资源）。该命令用于测试或者特殊运维场景下触发NG Reset流程。

## 操作本对象的命令

- [RST AN](command/UNC/20.15.2/RST-AN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位AN（RST-AN）_09653159.md`
