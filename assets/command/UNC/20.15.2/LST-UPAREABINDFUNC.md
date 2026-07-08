---
id: UNC@20.15.2@MMLCommand@LST UPAREABINDFUNC
type: MMLCommand
name: LST UPAREABINDFUNC（查询获取UPF服务区绑定TAI/LAI的方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPAREABINDFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- UP区域绑定方式
status: active
---

# LST UPAREABINDFUNC（查询获取UPF服务区绑定TAI/LAI的方式）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于查询获取UPF服务区绑定TAI/LAI的方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPAREABINDFUNC]] · 获取UPF服务区绑定TAI/LAI的方式（UPAREABINDFUNC）

## 使用实例

以下命令用于查询获取UPF服务区绑定TAI/LAI的方式： LST UPAREABINDFUNC:;

```
%%LST UPAREABINDFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                  生效方式 = 采用前缀的方式
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPAREABINDFUNC.md`
