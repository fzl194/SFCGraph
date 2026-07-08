---
id: UNC@20.15.2@MMLCommand@LST TAILAI
type: MMLCommand
name: LST TAILAI（查询TAI与LAI对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TAILAI
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- TAI与LAI对应关系
status: active
---

# LST TAILAI（查询TAI与LAI对应关系）

## 功能

**适用网元：MME**

该命令用于查询TAI与LAI的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 不输入任何参数则表示查询所有信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的跟踪区标识。<br>取值范围：9～10位的字符串<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询用户的范围。<br>前提条件：该参数在“<br>**选择模式**<br>”参数设置为“SUBRANGE(用户范围)”时，才需要配置。<br>取值范围：<br>- “ALL_USER（所有用户）”：无匹配IMSI前缀的所有用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：IMSI前缀最长长度优先匹配的用户。<br>- “IMSI_RANGE（指定IMSI范围）”:IMSI范围匹配用户<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询用户的IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，才需要配置。<br>取值范围：1～15位的数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：在参数在<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1~15位十进制数字字符串<br>默认值：无 |
| LAI | LAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的位置区标识。<br>取值范围：9～10位的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TAILAI]] · TAI与LAI对应关系（TAILAI）

## 使用实例

1. 查看 “TAI” 为 “308015101” ， “用户范围” 为 “IMSI_PREFIX（指定IMSI前缀）” ， “IMSI前缀” 为 “12345” 的对应关系：
  LST TAILAI: TAI="308015101", SUBRANGE=IMSI_PREFIX, IMSIPRE="12345";
  ```
  %%LST TAILAI: TAI="308015101", SUBRANGE=IMSI_PREFIX, IMSIPRE="12345";%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
   起始TAI  =  308015101
   终止TAI  =  308015101
  选择模式  =  用户范围
  用户范围  =  指定IMSI前缀
    主机名  =  NULL
      域名  =  NULL
  IMSI前缀  =  12345
  起始IMSI  =  NULL
  终止IMSI  =  NULL
       LAI  =  308010002
  (结果个数 = 1)

  ---    END
  ```
2. 查看系统中所有的TAI与LAI对应关系:
  LST TAILAI:;
  ```
  %%LST TAILAI:;%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
   起始TAI     终止TAI     选择模式 主机名 域名 用户范围      IMSI前缀    起始IMSI     终止IMSI       LAI      

   308014101   308014103   用户范围  NULL  NULL 所有用户      NULL        NULL        NULL          308010001
   308015101   308015101   用户范围  NULL  NULL 指定IMSI前缀  12345       NULL        NULL          308010002
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TAI与LAI对应关系(LST-TAILAI)_72225097.md`
