---
id: UNC@20.15.2@MMLCommand@LST CHRSNDPLCYCFG
type: MMLCommand
name: LST CHRSNDPLCYCFG（查询CHR传输策略控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRSNDPLCYCFG
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
- 移动性管理
- CHR管理
- CHR传输策略
status: active
---

# LST CHRSNDPLCYCFG（查询CHR传输策略控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询CHR传输策略控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRSNDPLCYCFG]] · CHR传输策略控制参数（CHRSNDPLCYCFG）

## 使用实例

查询CHR传输策略控制参数：

LST CHRSNDPLCYCFG:;

```
%%LST CHRSNDPLCYCFG:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
              CHR传输策略选择  =  自定义策略传输
未获取签约数据场景CHR传输开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHRSNDPLCYCFG.md`
