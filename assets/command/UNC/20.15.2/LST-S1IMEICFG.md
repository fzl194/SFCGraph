---
id: UNC@20.15.2@MMLCommand@LST S1IMEICFG
type: MMLCommand
name: LST S1IMEICFG（查询S1模式IMEI配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1IMEICFG
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
- 设备检查管理
- S1模式IMEI配置
status: active
---

# LST S1IMEICFG（查询S1模式IMEI配置）

## 功能

**适用网元：MME**

该命令用于查询EUTRAN用户获取和检查IMEI的策略。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划。<br>取值范围：<br>“ALL_USER（所有用户）”<br>、<br>“IMSI_PREFIX（指定IMSI前缀）”<br>、<br>“IMSI_RANGE（指定IMSI范围）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划。<br>取值范围：1~15位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1~15位十进制字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1IMEICFG]] · S1模式IMEI配置（S1IMEICFG）

## 使用实例

查询所有EUTRAN用户的IMEI配置：

LST S1IMEICFG:;

```
%%LST S1IMEICFG:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                         用户范围 = 所有用户
                         IMSI前缀 = NULL
                         起始IMSI = NULL
                         终止IMSI = NULL
                     IMEI获取策略 = 不获取
                     IMEI检查策略 = 不检查
                      EIR接口类型 = Gf
         IMEI获取失败是否允许接入 = 是
         IMEI检查超时是否允许接入 = 是
           是否允许灰名单用户接入 = 是
           是否允许黑名单用户接入 = 是
是否允许EIR返回用户原因失败时接入 = 是
是否允许EIR返回设备原因失败时接入 = 是
        是否允许EIR返回失败时接入 = 是
                  EIR响应超时时长 = 15
                     IMEI检查上限 = 0
                             描述 = 无

（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1IMEICFG.md`
