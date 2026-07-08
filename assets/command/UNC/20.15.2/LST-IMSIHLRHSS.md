---
id: UNC@20.15.2@MMLCommand@LST IMSIHLRHSS
type: MMLCommand
name: LST IMSIHLRHSS（查询IMSI对应的HLR/HSS接口）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIHLRHSS
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
- 业务安全管理
- 签约数据管理
- 接口选择
status: active
---

# LST IMSIHLRHSS（查询IMSI对应的HLR/HSS接口）

## 功能

**适用网元：SGSN、MME**

该命令用于查询IMSI对应的HLR/HSS接口。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIRANGE | IMSI范围 | 可选必选说明：可选参数<br>参数含义：该参数用于显示IMSI范围信息。<br>取值范围：<br>- “ALL IMSI（所有IMSI）”：表示该指定IMSI范围为所有IMSI。<br>- “SPECIAL IMSI （指定IMSI）”：表示该指定IMSI范围为指定IMSI。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀<br>前提条件：当<br>“IMSIRANGE（IMSI范围）”<br>设置为<br>“SPECIAL IMSI（指定IMSI）”<br>时有效。<br>取值范围：5～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIHLRHSS]] · IMSI对应的HLR/HSS接口（IMSIHLRHSS）

## 使用实例

1. 不输入查询IMSIRANGE查询当前已有的所有记录：
  LST IMSIHLRHSS:;
  ```
  %%LST IMSIHLRHSS:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
  IMSI范围    IMSI前缀    GERAN/UTRAN接入    E-UTRAN接入    GERAN/UTRAN接入APN签约上下文策略    E-UTRAN接入APN签约上下文策略    S6a融合网元指示    S6a/S6d融合网元指示    Intra CN节点单注册指示    Intra CN节点强制指示HSS单注册    Inter CN节点单注册指示    Inter CN节点强制指示HSS单注册

  所有IMSI    NULL        Gr                 S6a            优选GPRS APN签约上下文              优选EPS APN签约上下文           否                 NULL                   不启用                    ULR消息通知                      启用                      ULR消息通知                  
  指定IMSI    123456      Gr                 S6a            优选GPRS APN签约上下文              优选EPS APN签约上下文           否                 NULL                   不启用                    ULR消息通知                      启用                      ULR消息通知                  
  (结果个数 = 2)
  ---    END
  ```
2. 输入查询条件IMSIRANGE为SPECIAL_IMSI，IMSI前缀为123456：
  LST IMSIHLRHSS: IMSIRANGE=SPECIAL_IMSI, IMSIPRE="123456";
  ```
  %%LST IMSIHLRHSS: IMSIRANGE=SPECIAL_IMSI, IMSIPRE="123456";%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
                          IMSI范围  =  指定IMSI
                          IMSI前缀  =  123456
                   GERAN/UTRAN接入  =  Gr
                       E-UTRAN接入  =  S6a
  GERAN/UTRAN接入APN签约上下文策略  =  优选GPRS APN签约上下文
      E-UTRAN接入APN签约上下文策略  =  优选EPS APN签约上下文
                   S6a融合网元指示  =  否
               S6a/S6d融合网元指示  =  NULL
            Intra CN节点单注册指示  =  不启用
     Intra CN节点强制指示HSS单注册  =  ULR消息通知
            Inter CN节点单注册指示  =  启用
     Inter CN节点强制指示HSS单注册  =  ULR消息通知
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSIHLRHSS.md`
