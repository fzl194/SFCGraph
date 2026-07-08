---
id: UNC@20.15.2@MMLCommand@DSP UCFDISKSIZE
type: MMLCommand
name: DSP UCFDISKSIZE（显示ucfexec-pod的磁盘空间大小）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UCFDISKSIZE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF文件管理规格配置
status: active
---

# DSP UCFDISKSIZE（显示ucfexec-pod的磁盘空间大小）

## 功能

此命令用于查询ucfexec-pod的磁盘空间大小。

## 注意事项

执行命令前请确认UCF服务处于上线状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [ucfexec-pod的磁盘空间大小（UCFDISKSIZE）](configobject/UNC/20.15.2/UCFDISKSIZE.md)

## 使用实例

查询ucfexec-pod的磁盘空间：

```
%%DSP UCFDISKSIZE: ;%%
RETCODE = 0  操作成功

结果如下
--------
UCF Pod Id      UCF可用磁盘总空间(GB)

ucfexec-pod-0   64         
ucfexec-pod-1   64    
(结果个数 = 2)       

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示ucfexec-pod的磁盘空间大小（DSP-UCFDISKSIZE）_36880621.md`
