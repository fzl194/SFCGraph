---
id: UNC@20.15.2@MMLCommand@CMT MMLTRAN
type: MMLCommand
name: CMT MMLTRAN（提交配置）
nf: UNC
version: 20.15.2
verb: CMT
object_keyword: MMLTRAN
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 事务管理
status: active
---

# CMT MMLTRAN（提交配置）

## 功能

在启动事务模式后，期间下发的配置命令在执行该命令后才会真正生效。

## 注意事项

提交后的配置不再支持取消配置。

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMLTRAN]] · 取消配置（MMLTRAN）

## 使用实例

```
%%CMT MMLTRAN:;%%
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CMT-MMLTRAN.md`
