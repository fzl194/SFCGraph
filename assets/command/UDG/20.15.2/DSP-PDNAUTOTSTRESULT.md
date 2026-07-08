---
id: UDG@20.15.2@MMLCommand@DSP PDNAUTOTSTRESULT
type: MMLCommand
name: DSP PDNAUTOTSTRESULT（显示PDN自动探测结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PDNAUTOTSTRESULT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# DSP PDNAUTOTSTRESULT（显示PDN自动探测结果）

## 功能

**适用NF：PGW-U、UPF**

显示PDN自动探测结果。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的路径名称应满足路径名称的取值范围。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNAUTOTSTRESULT]] · PDN自动探测结果（PDNAUTOTSTRESULT）

## 使用实例

- 显示路径名为test1，探测方式为PING的PDN自动探测结果：
  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```
  ```

  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.1    DSCP:0    Probe mode:PING    Packet length:100
  Probed advertised route network segments:1    Successful:0    Failed:1    Probe status:completed
  Advertised route network segment info:
  --------------------------------------
  No.     Advertised Route Network Segment                Probe Result
  1       10.0.0.0/31                                     Failed
  (结果个数 = 1)

  ---    END
  ```
- 显示路径名为test1，探测方式为DNS的PDN自动探测结果：
  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```
  ```

  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:pool-test    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.10    DSCP:0    Probe mode:DNS    Domain name:
  Probed advertised route network segments:1    Successful:0    Failed:1    Probe status:completed
  Advertised route network segment info:
  --------------------------------------
  No.     Advertised Route Network Segment                Probe Result
  1       10.0.0.0/31                                     Failed
  (结果个数 = 1)

  ---    END
  ```
- 显示路径名为test1，探测方式为TRACERT的PDN自动探测结果：
  ```
  DSP PDNAUTOTSTRESULT: PATHNAME="test1";
  ```
  ```

  RETCODE = 0  Operation succeeded

  PDN侧路由自动探测结果信息
  ------------------------
                   Path Name  =  test1
  PDN Route Auto Test Result  =  
  Pool name:v4pool2    VPN-instance:NULL    Tigger Type:MML Command    Execute Time:2025-02-24 10:01:12    Destination IP address:10.1.1.10    DSCP:0    Probe mode:TRACERT
  Test hops:1    Probe status:completed
  Track 10.1.1.10 routing through up to 30 hops:
  No.     Gateway address                                                                     Probe packet delay        
  1       10.1.1.10 (10.1.1.10)                                                           20 ms     20 ms     10 ms
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PDN自动探测结果（DSP-PDNAUTOTSTRESULT）_64073335.md`
