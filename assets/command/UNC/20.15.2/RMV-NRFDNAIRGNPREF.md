---
id: UNC@20.15.2@MMLCommand@RMV NRFDNAIRGNPREF
type: MMLCommand
name: RMV NRFDNAIRGNPREF（删除DNAI区域优选规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFDNAIRGNPREF
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

# RMV NRFDNAIRGNPREF（删除DNAI区域优选规则）

## 功能

**适用NF：NRF**

该命令用于删除DNAI区域优选规则。该命令功能暂不生效。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>该参数配置为*时表示通配。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络访问标识符。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNAI区域优选规则（NRFDNAIRGNPREF）](configobject/UNC/20.15.2/NRFDNAIRGNPREF.md)

## 使用实例

当需要删除DNN为ims，DNAI为huawei.com的区域优选规则：

```
RMV NRFDNAIRGNPREF: DNN="ims", DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNAI区域优选规则（RMV-NRFDNAIRGNPREF）_43540613.md`
