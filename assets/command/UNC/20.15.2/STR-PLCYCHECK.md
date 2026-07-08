---
id: UNC@20.15.2@MMLCommand@STR PLCYCHECK
type: MMLCommand
name: STR PLCYCHECK（创建策略核查任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: PLCYCHECK
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# STR PLCYCHECK（创建策略核查任务）

## 功能

该命令用于创建一条mml优先级的策略核查任务，向app请求重新下发通信策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FORCE | 强制创建 | 可选必选说明：必选参数<br>参数含义：是否强制创建核查任务，当系统中存在正在进行的同类型的策略核查任务时，强制创建会开始一个新的核查任务，非强制则不会开始一个新的核查任务。<br>数据来源：本端规划<br>取值范围：<br>- YES（强制开始策略核查任务）<br>- NO（非强制策略核查）<br>默认值：无<br>配置原则：无 |
| PLCYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：策略类型，内部策略如Topic，RootToken等， 外部通信策略如VPN，LB策略等。<br>数据来源：本端规划<br>取值范围：<br>- Inner（内部策略）<br>- Outer（外部通信策略）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYCHECK]] · 创建策略核查任务（PLCYCHECK）

## 使用实例

使用如下命令强制创建一条外部通信策略的核查任务。

```
%%STR PLCYCHECK: FORCE=YES, PLCYTYPE=Outer;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            被创建任务的ID  =  m-6595
            核查任务是否成功创建  =  是
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-PLCYCHECK.md`
