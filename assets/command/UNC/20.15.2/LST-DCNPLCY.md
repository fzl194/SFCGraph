---
id: UNC@20.15.2@MMLCommand@LST DCNPLCY
type: MMLCommand
name: LST DCNPLCY（查询DCN配置策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DCNPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN配置策略
status: active
---

# LST DCNPLCY（查询DCN配置策略）

## 功能

**适用网元：MME**

该命令用于查询不同范围内用户的DCN配置策略参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加DCN策略的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PRE(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PRE(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DCNPLCY]] · DCN配置策略（DCNPLCY）

## 使用实例

1. 查询 “IMSI前缀” 为 “123003” 的用户的DCN策略参数：
  LST DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003";
  ```
  %%LST DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003";%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
               用户范围  =  指定IMSI前缀
               IMSI前缀  =  123003
                DCN开关  =  打开
  源侧UE USAGE TYPE策略  =  是
  UE USAGE TYPE获取策略  =  本地获取
          UE USAGE TYPE  =  100
           网关选择策略  =  使用
  (结果个数 = 1)

  ---    END
  ```
2. 查询配置表中所有用户的DCN策略参数：
  LST DCNPLCY:;
  ```
  %%LST DCNPLCY:;%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
   用户范围      IMSI前缀  DCN开关  源侧UE USAGE TYPE策略  UE USAGE TYPE获取策略  UE USAGE TYPE   网关选择策略

   指定IMSI前缀  123003    打开     是                     本地获取               100             使用      
   所有用户      NULL      打开     是                     HSS获取                NULL            使用
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DCNPLCY.md`
