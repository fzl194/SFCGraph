---
id: UNC@20.15.2@MMLCommand@LST RESTOUSRSEG
type: MMLCommand
name: LST RESTOUSRSEG（查询容灾用户号段参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESTOUSRSEG
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾用户号段管理
status: active
---

# LST RESTOUSRSEG（查询容灾用户号段参数）

## 功能

**适用网元：MME**

此命令用于查询容灾用户号段参数配置。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链式备份功能服务的用户范围。<br>取值范围：<br>- IMSI_PREFIX(指定IMSI前缀)<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 必选说明：条件必选参数<br>参数含义：该参数用于指定链式备份功能服务的用户范围的IMSI前缀。<br>前提条件：该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”后生效。<br>数据来源：全网规划<br>取值范围：5～15位十进制数字字符串。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOUSRSEG]] · 容灾用户号段参数（RESTOUSRSEG）

## 使用实例

1. 查询容灾用户号段参数配置，可以用如下命令：
  LST RESTOUSRSEG:;
  ```
  %%LST RESTOUSRSEG:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
       用户范围  =  指定IMSI前缀
       IMSI前缀  =  12345
   是否备份用户  =  是
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾用户号段参数-(LST-RESTOUSRSEG)_10554145.md`
