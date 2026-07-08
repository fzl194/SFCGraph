---
id: UNC@20.15.2@MMLCommand@LST N26IWKPLCY
type: MMLCommand
name: LST N26IWKPLCY（查询EPS与5GS互操作本地策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N26IWKPLCY
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
- N26互操作策略
status: active
---

# LST N26IWKPLCY（查询EPS与5GS互操作本地策略）

## 功能

**适用网元：MME**

该命令用于5GS部署时，查询用户的EPS与5GS互操作本地策略。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置EPS与5GS互操作策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：表示用户范围为系统内所有用户。<br>- “HOME_USER（本网用户）”：表示用户范围为本网用户。<br>- “FOREIGN_USER（外网用户）”：表示用户范围为外网用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：表示用户范围通过IMSI前缀指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定待配置EPS与5GS互操作控制策略用户的IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N26IWKPLCY]] · EPS与5GS互操作本地策略（N26IWKPLCY）

## 使用实例

1. 查询所有记录：
  LST N26IWKPLCY:;
  ```
  %%LST N26IWKPLCY:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  用户范围        运营商标识    IMSI前缀      是否支持接入5GC    是否允许接入5GS的NR    融合PGW-C/SMF选择策略    5GSIWK策略    5GCNRS策略    描述信息

  所有用户        NULL          NULL          是                 是                     N1能力+签约CNR           SMF融合网关   不支持        123456  
  本网用户        0             NULL          是                 是                     N1能力+签约CNR           SMF融合网关   不支持        1234567 
  外网用户        128           NULL          是                 是                     N1能力+签约CNR           SMF融合网关   不支持        12345678
  指定IMSI前缀    NULL          9876543210    是                 是                     N1能力+签约CNR           SMF融合网关   不支持        12345678
  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N26IWKPLCY.md`
