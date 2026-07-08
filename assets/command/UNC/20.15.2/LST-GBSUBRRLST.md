---
id: UNC@20.15.2@MMLCommand@LST GBSUBRRLST
type: MMLCommand
name: LST GBSUBRRLST（查询Gb模式用户漫游限制列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBSUBRRLST
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- Gb模式用户漫游限制管理
status: active
---

# LST GBSUBRRLST（查询Gb模式用户漫游限制列表）

## 功能

**适用网元：SGSN**

该命令用于查询Gb模式用户漫游限制列表。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>- “ALL_USER（所有用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>说明：- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>对于外网用户，该参数是外网用户对应的签订互联PLMN漫游协议的运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBSUBRRLST]] · Gb模式用户漫游限制列表（GBSUBRRLST）

## 使用实例

查询Gb模式所有的漫游限制列表记录：

LST GBSUBRRLST:;

```
%%LST GBSUBRRLST:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
    用户范围  =  指定IMSI前缀
    IMSI前缀  =  123456
    起始IMSI  =  NULL
    终止IMSI  =  NULL
  运营商标识  =  NULL
  区域群标识  =  55
区域限制模式  =  黑名单
  拒绝原因值  =  本地无合适小区
自定义原因值  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Gb模式用户漫游限制列表(LST-GBSUBRRLST)_26145548.md`
