---
id: UNC@20.15.2@MMLCommand@LST DMOCCFG
type: MMLCommand
name: LST DMOCCFG（查询Diameter流控控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMOCCFG
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Diameterl流控管理
status: active
---

# LST DMOCCFG（查询Diameter流控控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询Diameter流控控制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMOCCFG]] · Diameter流控控制参数（DMOCCFG）

## 使用实例

查询普通计费属性的配置信息：

LST DMOCCFG:;

```
%%LST DMOCCFG:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
 Diameter流控Sequence Number有效变化门限值  =  367778
             Diameter流控导致ULR拒绝原因值  =  53
             Diameter流控导致AIR拒绝原因值  =  45
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMOCCFG.md`
