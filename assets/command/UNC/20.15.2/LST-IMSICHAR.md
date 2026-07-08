---
id: UNC@20.15.2@MMLCommand@LST IMSICHAR
type: MMLCommand
name: LST IMSICHAR（查询IMSI号段属性配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSICHAR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- IMSI号段属性配置表
status: active
---

# LST IMSICHAR（查询IMSI号段属性配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查询IMSI号段对应的属性配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：待查询签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：待查询IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：待查询IMSI，对该IMSI所在号段进行查询<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IMSI号段属性配置（IMSICHAR）](configobject/UNC/20.15.2/IMSICHAR.md)

## 使用实例

查询所有IMSI号段对应的属性配置记录：

LST IMSICHAR:;

```
%%LST IMSICHAR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
       用户范围  =  所有用户
       IMSI前缀  =  NULL
       起始IMSI  =  NULL
       终止IMSI  =  NULL
     本局SGSN号  =  NULL
   本地实体索引  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI号段属性配置(LST-IMSICHAR)_26146052.md`
