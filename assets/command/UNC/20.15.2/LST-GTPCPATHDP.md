---
id: UNC@20.15.2@MMLCommand@LST GTPCPATHDP
type: MMLCommand
name: LST GTPCPATHDP（查询GTP-C路径管理自定义策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCPATHDP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径管理自定义策略
status: active
---

# LST GTPCPATHDP（查询GTP-C路径管理自定义策略）

## 功能

**适用网元：SGSN**

该命令用于查询GTP-C路径管理自定义策略。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 路径范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C路径范围。<br>取值范围：<br>- ROAMING（漫游路径）<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHDP]] · GTP-C路径管理自定义策略（GTPCPATHDP）

## 使用实例

查询GTP-C路径管理自定义策略：

LST GTPCPATHDP:;

```
%%LST GTPCPATHDP:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
          路径范围  =  漫游路径
  故障判定钝化系数  =  2
漫游路径告警ID控制  =  公共告警ID
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPCPATHDP.md`
