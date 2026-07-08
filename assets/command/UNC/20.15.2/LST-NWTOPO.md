---
id: UNC@20.15.2@MMLCommand@LST NWTOPO
type: MMLCommand
name: LST NWTOPO（查询组网拓扑采集功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NWTOPO
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
- 系统管理
- 系统维护
- 组网拓扑功能
status: active
---

# LST NWTOPO（查询组网拓扑采集功能开关）

## 功能

**适用网元：SGSN、MME**

该命令用于显示组网拓扑信息采集功能是否打开。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NWTOPO]] · 组网拓扑采集功能开关（NWTOPO）

## 使用实例

查询组网拓扑采集功能开关状态，运行命令如下：

LST NWTOPO:;

```
%%LST NWTOPO:;%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
拓扑采集功能  =  去使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NWTOPO.md`
