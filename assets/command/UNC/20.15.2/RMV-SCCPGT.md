---
id: UNC@20.15.2@MMLCommand@RMV SCCPGT
type: MMLCommand
name: RMV SCCPGT（删除SCCP全局翻译码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCCPGT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP全局翻译码
status: active
---

# RMV SCCPGT（删除SCCP全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP全局码翻译表中指定记录的信息。

## 注意事项

- 此命令执行后立即生效。
- 删除GT码可能会导致原来使用这条GT码的消息翻译错误或者无法翻译，请谨慎使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTX | GT码索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定希望要被删除的GT码索引。取值范围：0~4095<br>默认值：无<br>说明：此索引对应的GT记录应该在GT表中存在。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPGT]] · SCCP全局翻译码（SCCPGT）

## 使用实例

以下命令删除SCCP全局码翻译表中索引1记录的信息：

RMV SCCPGT: GTX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCCP全局翻译码(RMV-SCCPGT)_72345925.md`
