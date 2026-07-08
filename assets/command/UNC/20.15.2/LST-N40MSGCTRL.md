---
id: UNC@20.15.2@MMLCommand@LST N40MSGCTRL
type: MMLCommand
name: LST N40MSGCTRL（查询N40接口消息的控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40MSGCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST N40MSGCTRL（查询N40接口消息的控制参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询N40接口消息的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N40MSGCTRL]] · N40接口消息的控制参数（N40MSGCTRL）

## 使用实例

查询N40接口消息的控制参数：

```
%%LST N40MSGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
      国际漫游场景更新流程中仅离线新业务预申请上报CHF开关  =  不使能
                             GERAN/UTRAN接入场景携带UPFID  =  使能
GERAN/UTRAN接入场景携带Presence Reporting Area Infomation  =  使能
       GERAN/UTRAN接入场景携带Network Slicing Information  =  使能
                          GERAN/UTRAN接入场景携带SSC Mode  =  使能
                GERAN/UTRAN接入场景携带DNN Selection Mode  =  使能
            GERAN/UTRAN接入场景携带Session Stop Indicator  =  使能
       GERAN/UTRAN接入场景携带Unit Count Inactivity Timer  =  使能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N40MSGCTRL.md`
