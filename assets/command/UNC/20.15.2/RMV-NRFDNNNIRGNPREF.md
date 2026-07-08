---
id: UNC@20.15.2@MMLCommand@RMV NRFDNNNIRGNPREF
type: MMLCommand
name: RMV NRFDNNNIRGNPREF（删除DNNNI区域优选规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFDNNNIRGNPREF
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF区域优选管理
status: active
---

# RMV NRFDNNNIRGNPREF（删除DNNNI区域优选规则）

## 功能

**适用NF：NRF**

该命令用于删除DNNNI区域优选规则。该命令功能暂不生效。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示DNN网络标识。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFDNNNIRGNPREF]] · DNNNI区域优选规则（NRFDNNNIRGNPREF）

## 使用实例

当运营商需要删除DNNNI为huawei.com的区域优选规则：

```
RMV NRFDNNNIRGNPREF: DNNNI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFDNNNIRGNPREF.md`
