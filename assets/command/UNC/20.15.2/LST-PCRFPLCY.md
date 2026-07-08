---
id: UNC@20.15.2@MMLCommand@LST PCRFPLCY
type: MMLCommand
name: LST PCRFPLCY（查询PCRF策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCRFPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- PCRF策略管理
status: active
---

# LST PCRFPLCY（查询PCRF策略）

## 功能

**适用网元：MME**

该命令用于查询PCRF策略。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFPLCY]] · PCRF策略（PCRFPLCY）

## 使用实例

查询设置的PCRF策略：

LST PCRFPLCY:;

```
%%LST PCRFPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
  灵活选频功能开关  =  
YES

          默认RFSP  =  
1

是否使用对等口RFSP  =  
YES

是否开启动态NI功能  =  
YES

        运营商全称  =  
aaa

        运营商简称  =  
a

  是否使用对等口NI  =  
NO

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCRF策略（LST-PCRFPLCY）_09214818.md`
