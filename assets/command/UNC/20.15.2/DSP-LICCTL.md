---
id: UNC@20.15.2@MMLCommand@DSP LICCTL
type: MMLCommand
name: DSP LICCTL（查询紧急License状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LICCTL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP LICCTL（查询紧急License状态信息）

## 功能

该命令用于查询系统当前License紧急状态信息。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LICCTL]] · 紧急License（LICCTL）

## 使用实例

License处于紧急状态时：

```
%%DSP LICCTL:;%%
RETCODE = 0  操作成功

License紧急信息
---------------
           License紧急状态  =  打开
距离自动关闭启动紧急的天数  =  6
          剩余启动紧急次数  =  2
(结果个数 = 1)

---    END 
```

License处于非紧急状态时：

```
%%DSP LICCTL:;%%
RETCODE = 0  操作成功

License紧急信息
---------------
           License紧急状态  =  关闭
距离自动关闭启动紧急的天数  =  NULL
          剩余启动紧急次数  =  2  
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LICCTL.md`
