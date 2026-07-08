---
id: UNC@20.15.2@MMLCommand@RMV GBNSECFGPARA
type: MMLCommand
name: RMV GBNSECFGPARA（删除NSE属性模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBNSECFGPARA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性模板管理
status: active
---

# RMV GBNSECFGPARA（删除NSE属性模板）

## 功能

**适用网元：SGSN**

此命令用于删除NSE属性模板。

## 注意事项

- 此命令执行后，原来所设置的参数“信令权重”和“数据权重”要在BSC重新发起动态建链流程后才能对自动配置的NSE生效，原来所设置的NSE其他属性参数将采用默认模板的配置。
- 删除NSE属性模板记录前，请执行[**LST GBNSEGRP**](../NSE属性管理/查询NSE和属性模板的关联(LST GBNSEGRP)_26305812.md)命令，确认GBNSEGRP数据表中是否存在此模板索引相关的记录，如果存在将不允许删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAINDEX | 模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的NSE属性模板的索引。<br>取值范围：0～65535<br>默认值：无<br>说明：0表示系统默认添加的属性模板，不能被删除。 |

## 操作的配置对象

- [NSE属性模板（GBNSECFGPARA）](configobject/UNC/20.15.2/GBNSECFGPARA.md)

## 使用实例

删除 “模板索引 ” 为 “1” 的NSE属性模板：

RMV GBNSECFGPARA: PARAINDEX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NSE属性模板(RMV-GBNSECFGPARA)_72225683.md`
