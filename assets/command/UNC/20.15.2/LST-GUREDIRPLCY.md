---
id: UNC@20.15.2@MMLCommand@LST GUREDIRPLCY
type: MMLCommand
name: LST GUREDIRPLCY（查询GU重定向策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GUREDIRPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- GU重定向策略管理
status: active
---

# LST GUREDIRPLCY（查询GU重定向策略）

## 功能

**适用网元：MME**

该命令用于查询GU重定向策略。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域的标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “PLMN(PLMN)”：表示该区域标识类型为指定PLMN区域。<br>- “TA(指定跟踪区)”：表示该区域标识类型为指定跟踪区。<br>默认值：无<br>说明：本表“区域范围”为“PLMN(PLMN)”的记录可以与“区域范围”为“TA(指定跟踪区)”的记录共存；“区域范围”为“TA(指定跟踪区)”的记录优先级更高。 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定移动国家代码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>或者<br>“PLMN(PLMN)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定移动网号。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>或者<br>“PLMN(PLMN)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“TA(指定跟踪区)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GUREDIRPLCY]] · GU重定向策略（GUREDIRPLCY）

## 使用实例

查询GU重定向策略:

LST GUREDIRPLCY:;

```
%%LST GUREDIRPLCY:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
            区域范围  =  PLMN
          移动国家码  =  460
            移动网号  =  01
          跟踪区域码  =  NULL
      跟踪区域码范围  =  NULL
   redir-policy 取值  = 
Unsecured redirection to GERAN or UTRAN allowed

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GU重定向策略（LST-GUREDIRPLCY）_36144465.md`
