---
id: UNC@20.15.2@MMLCommand@ADD HLRBPFAULTCODE
type: MMLCommand
name: ADD HLRBPFAULTCODE（增加HLR BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HLRBPFAULTCODE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HLR BYPASS故障状态码
status: active
---

# ADD HLRBPFAULTCODE（增加HLR BYPASS故障状态码）

## 功能

**适用网元：SGSN**

本命令用于添加HLR BYPASS故障状态码配置。当希望HLR全故障后，系统收到HLR/DRA返回某个特定原因值时，用户进入HLR BYPASS状态，可通过此命令配置该原因值为HLR BYPASS原因值。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为512。
- 通过Inter流程接入的用户，在域路由组网方式下，由于SGSN无法获取到HLR局向，该场景只有“ALL（整系统）”配置生效。
- 主备HLR网元都故障时，可针对故障的网元增加BYPASS故障码。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特定故障码的生效范围。<br>取值范围：<br>- ALL（整系统）：整系统 |
| FAULTCODE | 故障码 | 可选必选说明：必选参数<br>参数含义：<br>该参数用于指定进入HLR BYPASS状态的原因值。<br>取值范围：0-65535<br>默认值：无 |

## 操作的配置对象

- [HLR BYPASS故障状态码（HLRBPFAULTCODE）](configobject/UNC/20.15.2/HLRBPFAULTCODE.md)

## 使用实例

增加HLR BYPASS故障状态码配置，生效范围为ALL（整系统），故障码为3002。

```
ADD HLRBPFAULTCODE: RANGE=ALL, FAULTCODE=3002;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加HLR-BYPASS故障状态码(ADD-HLRBPFAULTCODE)_04923686.md`
