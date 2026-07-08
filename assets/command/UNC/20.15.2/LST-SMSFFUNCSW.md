---
id: UNC@20.15.2@MMLCommand@LST SMSFFUNCSW
type: MMLCommand
name: LST SMSFFUNCSW（查询SMSF功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFFUNCSW
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSF功能开关
status: active
---

# LST SMSFFUNCSW（查询SMSF功能开关）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF的功能开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFFUNCSW]] · SMSF功能开关（SMSFFUNCSW）

## 使用实例

运营商希望查询SMSF功能开关，执行如下命令：

```
LST SMSFFUNCSW:;
%%LST SMSFFUNCSW:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
                    SMSF向注册中心注册开关  =  打开
                      SMSF内部统计功能开关  =  打开
                   SMSF是否向UDM显式去订阅  =  打开
         SMSF向UDM显式去订阅超时时限(分钟)  =  1440
                 转发MO消息携带ULI信息开关  =  打开
                   SMSF向UDM续订阅功能开关  =  打开
                   SMSF向UDM续订阅冗余时长  =  120
优先使用AMF Binding头域重选备份AMF功能开关  =  打开
                           转发NCG告警开关  =  打开
                       NCG告警核查恢复时长  =  30
                   NCG告警内部资源核查开关  =  打开
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF功能开关（LST-SMSFFUNCSW）_04121605.md`
