---
id: UNC@20.15.2@MMLCommand@LST FASTRECOVERY
type: MMLCommand
name: LST FASTRECOVERY（查询全局业务快速恢复配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FASTRECOVERY
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- 全局参数
status: active
---

# LST FASTRECOVERY（查询全局业务快速恢复配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于显示业务快速恢复功能的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/FASTRECOVERY]] · 全局业务快速恢复配置（FASTRECOVERY）

## 使用实例

当用户需要查询快速业务恢复功能配置时：

```
%%LST FASTRECOVERY:;%%
RETCODE = 0  操作成功

结果如下
--------
          防闪断定时器时长(秒)  =  120
      保留承载的超时时长(分钟)  =  59
网络侧触发业务恢复功能功能开关  =  不使能
   故障重启业务恢复功能PGW开关  =  不使能
                  PDTN功能开关  =  不使能
   故障重启业务恢复功能SGW开关  =  不使能
              PDTN广播功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FASTRECOVERY.md`
