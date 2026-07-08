---
id: UNC@20.15.2@MMLCommand@LST N26GWSELPLCY
type: MMLCommand
name: LST N26GWSELPLCY（查询N26融合网关选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N26GWSELPLCY
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
- N26互操作管理
- N26融合网关选择策略
status: active
---

# LST N26GWSELPLCY（查询N26融合网关选择策略）

## 功能

**适用网元：MME**

该命令用于LTE和5G互通组网部署时，查询5G用户的融合PGW-C/SMF选择策略。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置融合PGW-C/SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定待配置融合PGW-C/SMF选择策略用户的IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无 |

## 操作的配置对象

- [N26融合网关选择策略（N26GWSELPLCY）](configobject/UNC/20.15.2/N26GWSELPLCY.md)

## 使用实例

1. 查询所有记录：
  LST N26GWSELPLCY:;
  ```
  %%LST N26GWSELPLCY:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------------------
    用户范围  =  指定IMSI前缀
  运营商标识  =  NULL
    IMSI前缀  =  12345679
       APNNI  =  HUAWEILAC
    定制标识  =  HUAWEI
    描述信息  =  test
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N26融合网关选择策略(LST-N26GWSELPLCY)_26305948.md`
