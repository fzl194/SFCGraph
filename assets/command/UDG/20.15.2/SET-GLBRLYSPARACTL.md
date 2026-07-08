---
id: UDG@20.15.2@MMLCommand@SET GLBRLYSPARACTL
type: MMLCommand
name: SET GLBRLYSPARACTL（设置媒体中继全局业务参数控制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBRLYSPARACTL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继全局业务参数控制
status: active
---

# SET GLBRLYSPARACTL（设置媒体中继全局业务参数控制）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置媒体中继全局业务参数控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | UESRVWAITTIME | CDNSRVWAITTM | VODMAXDATASIZE | CDNIPWAITTIME | ORIGINRETRYTMS | MAXORIGINRDTMS | DNSFTTRYTM | DNSRSPETRYTM | MAXDNSIDLETM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 15 | 5 | 20 | 5 | 2 | 3 | 5 | 30 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UESRVWAITTIME | 用户业务等待时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定UE业务等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~30，单位为秒。<br>默认值：无<br>配置原则：无 |
| CDNSRVWAITTM | 回源业务数据等待时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源业务数据等待时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~30，单位为秒。<br>默认值：无<br>配置原则：无 |
| VODMAXDATASIZE | 点播推流最大数据块（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用来指定每次点播业务推送的最大数据块。每5ms推送一次点播业务数据，实际推送的数据块大小受限于TCP发送窗口状态。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~50，单位为千字节。<br>默认值：无<br>配置原则：无 |
| CDNIPWAITTIME | 获取CDNIP的最大等待时长（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定获取CDNIP最大等待时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2~30，单位为秒。<br>默认值：无<br>配置原则：无 |
| ORIGINRETRYTMS | 回源重试次数（次数） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源重试次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~5，单位为次数。<br>默认值：无<br>配置原则：无 |
| MAXORIGINRDTMS | 回源重定向最大次数（次数） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源重定向最大次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~5，单位为次数。<br>默认值：无<br>配置原则：无 |
| DNSFTTRYTM | 回源DNS服务器故障重试间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源DNS服务器故障重试间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~600，单位为秒。<br>默认值：无<br>配置原则：无 |
| DNSRSPETRYTM | 回源DNS响应异常最小重试间隔（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源DNS响应异常最小重试间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~600，单位为秒。<br>默认值：无<br>配置原则：无 |
| MAXDNSIDLETM | 回源DNS记录最大空闲时长（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用来指定回源DNS记录最大空闲时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~1440，单位为分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBRLYSPARACTL]] · 媒体中继全局业务参数控制（GLBRLYSPARACTL）

## 使用实例

假如需要创建配置媒体中继全局业务参数控制，则命令如下：

```
SET GLBRLYSPARACTL: UESRVWAITTIME=10, VODMAXDATASIZE=20, CDNIPWAITTIME=10, ORIGINRETRYTMS=2, MAXORIGINRDTMS=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置媒体中继全局业务参数控制（SET-GLBRLYSPARACTL）_43992606.md`
