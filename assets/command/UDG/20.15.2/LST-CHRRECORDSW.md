---
id: UDG@20.15.2@MMLCommand@LST CHRRECORDSW
type: MMLCommand
name: LST CHRRECORDSW（查询CHR本地存盘开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CHRRECORDSW
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 呼叫日志管理
- CHR本地存盘开关配置
status: active
---

# LST CHRRECORDSW（查询CHR本地存盘开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用来查询当前的CHR本地存盘开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CHR本地存盘开关（CHRRECORDSW）](configobject/UDG/20.15.2/CHRRECORDSW.md)

## 使用实例

查询CHRRECORDSW内容：

```
LST CHRRECORDSW:;
```

```

RETCODE = 0  操作成功

CHR上报本地存储错误类型
-----------------------
本地存盘错误类型开关  =  偶连建立失败&偶连删除失败&偶连更新失败&节点上报失败&会话建立失败&会话删除失败&会话更新失败&会话上报失败&宽带集群承载创建失败&宽带集群承载删除失败&宽带集群eNB激活失败&宽带集群eNB删除失败&宽带集群eNB删除上报失败&宽带集群会话建立失败&宽带集群会话删除失败
(结果个数 = 1)

---   结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CHR本地存盘开关（LST-CHRRECORDSW）_53604161.md`
