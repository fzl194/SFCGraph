---
id: UNC@20.15.2@MMLCommand@DSP LBTOPO
type: MMLCommand
name: DSP LBTOPO（查询SDRC中缓存的CSLB的拓扑）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBTOPO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP LBTOPO（查询SDRC中缓存的CSLB的拓扑）

## 功能

该命令用于查询SDRC中缓存的CSLB的拓扑。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [SDRC中缓存的CSLB的拓扑（LBTOPO）](configobject/UNC/20.15.2/LBTOPO.md)

## 使用实例

查询SDRC中缓存的CSLB拓扑，结果如下：

```
%%DSP LBTOPO:;%%
RETCODE = 0  操作成功

结果如下
--------
High TB  Low TB  TP          组 ID

0       1109   2416123937  4        
0       1121   2416123937  4        
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SDRC中缓存的CSLB的拓扑（DSP-LBTOPO）_94730409.md`
