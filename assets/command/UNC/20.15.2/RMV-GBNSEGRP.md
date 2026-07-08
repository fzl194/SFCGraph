---
id: UNC@20.15.2@MMLCommand@RMV GBNSEGRP
type: MMLCommand
name: RMV GBNSEGRP（删除NSE和属性模板的关联）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBNSEGRP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性管理
status: active
---

# RMV GBNSEGRP（删除NSE和属性模板的关联）

## 功能

**适用网元：SGSN**

此命令用于删除NSE和属性模板的关联。删除此关联后，NSE使用默认属性模板里的NSE属性，NSE重新上报后生效，默认属性模板的模板索引号为0。

## 注意事项

- 此命令执行后立即生效。
- 执行此命令后，不影响当前NSE的属性，下次NSE重新上报后生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPINDEX | 关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除关联的索引。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBNSEGRP]] · NSE和属性模板的关联（GBNSEGRP）

## 使用实例

删除一组NSE到属性模板的关联， “关联索引” 为 “0” ：

RMV GBNSEGRP: GRPINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GBNSEGRP.md`
