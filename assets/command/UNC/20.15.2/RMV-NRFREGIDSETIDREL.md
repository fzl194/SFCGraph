---
id: UNC@20.15.2@MMLCommand@RMV NRFREGIDSETIDREL
type: MMLCommand
name: RMV NRFREGIDSETIDREL（删除AMF区域标识和集合标识的关联关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFREGIDSETIDREL
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- AMF区域标识路由管理
status: active
---

# RMV NRFREGIDSETIDREL（删除AMF区域标识和集合标识的关联关系）

## 功能

**适用NF：NRF**

该命令用于在NRF上删除AMF区域标识和集合标识的关联关系。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFREGID | AMF区域标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF区域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时从左边补0，取值范围0~ff。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF集合标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时从左边补0，取值范围0~3ff。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF区域标识和集合标识的关联关系（NRFREGIDSETIDREL）](configobject/UNC/20.15.2/NRFREGIDSETIDREL.md)

## 使用实例

运营商想在PLMN-NRF上删除AMF区域标识和集合标识的关联关系，配置此命令。

```
RMV NRFREGIDSETIDREL: AMFREGID="09", AMFSETID="123";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF区域标识和集合标识的关联关系（RMV-NRFREGIDSETIDREL）_09651341.md`
