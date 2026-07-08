---
id: UNC@20.15.2@MMLCommand@LST IUCONNPARA
type: MMLCommand
name: LST IUCONNPARA（查询Iu连接控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUCONNPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- Iu连接控制参数
status: active
---

# LST IUCONNPARA（查询Iu连接控制参数）

## 功能

**适用网元：SGSN**

该命令用于查询Iu连接控制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUCONNPARA]] · Iu连接控制参数（IUCONNPARA）

## 使用实例

查询IUCONNPARA参数：

LST IUCONNPARA:;

```
%%LST IUCONNPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------
   Follow on without PDP场景Iu连接管理 (s)  =  10
      Follow on with PDP场景Iu连接管理 (s)  =  10
No follow on without PDP场景Iu连接管理 (s)  =  0
   No follow on with PDP场景Iu连接管理 (s)  =  0
                      SMS流程Iu连接管理(s)  =  65535
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IUCONNPARA.md`
