---
id: UNC@20.15.2@MMLCommand@MOD PLMNNS
type: MMLCommand
name: MOD PLMNNS（修改网络切片）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PLMNNS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- PLMN内网络切片管理
status: active
---

# MOD PLMNNS（修改网络切片）

## 功能

**适用NF：AMF、SMF、SMSF**

该命令用于修改指定网络切片的状态等信息。

## 注意事项

- 该命令执行后立即生效。

- 修改网络切片时，需要新增或修改对应的DNN纠正配置（ADD LOCALNSDNN/MOD LOCALNSDNN），防止因DNN不匹配导致用户会话建立失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用以在系统内唯一标识某个网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| STATE | 状态 | 可选必选说明：可选参数<br>参数含义：该参数表示网络切片的状态：未激活或者已激活。只有处于激活状态的网络切片才能被UE使用。<br>数据来源：全网规划<br>取值范围：<br>- “INACTIVE（未激活）”：网络切片未激活<br>- “ACTIVE（激活）”：网络切片已激活<br>默认值：无<br>配置原则：<br>当由于切片用户欠费、网络运维等原因需要临时停止使用指定的网络切片时，将本参数值设置为“INACTIVE”；当指定的网络切片可用时，将本参数值设置为“ACTIVE”。<br>另，切片状态及其变化不影响NF到NRF的注册过程，不影响SMF的会话管理但影响MB-SMF的广播会话管理和组播会话管理。 |
| NSSCOPE | 网络切片生效范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示网络切片的生效范围。<br>数据来源：全网规划<br>取值范围：<br>- “GLOBALNW（全局网络）”：网络切片在运营商全网范围内生效。<br>- “CAMPUSNW（园区网络）”：网络切片在运营商网络的局部范围内生效，具体的范围依赖于运营商的网络切片规划。<br>默认值：无<br>配置原则：<br>根据运营商对网络切片的规划进行配置。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对网络切片的描述，在运维中起助记作用。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNNS]] · 网络切片（PLMNNS）

## 使用实例

修改指定网络切片的标识，执行如下命令：

```
MOD PLMNNS: NSIDX=0, STATE=ACTIVE, DESC="for TAXI";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PLMNNS.md`
