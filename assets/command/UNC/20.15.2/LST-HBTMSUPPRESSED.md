---
id: UNC@20.15.2@MMLCommand@LST HBTMSUPPRESSED
type: MMLCommand
name: LST HBTMSUPPRESSED（查询NRF心跳超时抑制时长）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HBTMSUPPRESSED
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 定时器参数
status: active
---

# LST HBTMSUPPRESSED（查询NRF心跳超时抑制时长）

## 功能

**适用NF：NRF**

该命令用于查询NRF心跳超时抑制时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HBTMSUPPRESSED]] · NRF心跳超时抑制时长（HBTMSUPPRESSED）

## 使用实例

当运营商希望查询心跳超时抑制时长时，执行此命令。

```
LST HBTMSUPPRESSED:;
%%LST HBTMSUPPRESSED:;%%
RETCODE = 0  操作成功
结果如下
-------------------------
 心跳超时抑制时长(秒)  				    =  200
 双活断链恢复后心跳超时抑制时长(秒)   = 660
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HBTMSUPPRESSED.md`
