---
id: UNC@20.15.2@MMLCommand@LST IUSMPROCTRL
type: MMLCommand
name: LST IUSMPROCTRL（查询Iu模式SM流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUSMPROCTRL
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM流程管理
- Iu模式SM流程控制参数
status: active
---

# LST IUSMPROCTRL（查询Iu模式SM流程控制参数）

## 功能

**适用网元：SGSN**

该命令用于查询Iu模式SM流程控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>取值范围：<br>- “ACT_PROC(激活流程)”<br>- “MOD_PROC(修改流程)”<br>- “HSS_INIT_SUB_QOS_MOD_PROC(HSS发起的签约QoS修改流程)”<br>默认值：无<br>说明：若不输入流程类型，则将显示所有流程类型的原因值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUSMPROCTRL]] · Iu模式SM流程控制参数（IUSMPROCTRL）

## 使用实例

查询Iu模式SM流程控制参数：

LST IUSMPROCTRL:;

```
%%LST IUSMPROCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
激活拒绝原因值（GGSN超时）  =  30
激活拒绝原因值（GGSN拒绝）  =  0
修改拒绝原因值（GGSN拒绝）  =  0
    当RAB修改失败时删除PDP  =  否
          是否使用保留带宽  =  是
       签约QoS变更判断策略  =  与正在使用的QoS比较
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IUSMPROCTRL.md`
