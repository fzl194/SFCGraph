---
id: UNC@20.15.2@MMLCommand@DSP VPROBEDISKSIZE
type: MMLCommand
name: DSP VPROBEDISKSIZE（显示vprobeexec-pod的磁盘空间大小）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VPROBEDISKSIZE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe文件管理规格配置
status: active
---

# DSP VPROBEDISKSIZE（显示vprobeexec-pod的磁盘空间大小）

## 功能

此命令用于查询vprobeexec-pod的磁盘空间大小。

## 注意事项

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPROBEDISKSIZE]] · vprobeexec-pod的磁盘空间大小（VPROBEDISKSIZE）

## 使用实例

查询vprobeexec-pod的磁盘空间：

```
%%DSP VPROBEDISKSIZE:;%%
RETCODE = 0  操作成功

结果如下
--------
vProbe Pod ID     vProbe可用磁盘总空间(GB)  

vprobeexec-pod-0  64                        
vprobeexec-pod-1  64                        
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-VPROBEDISKSIZE.md`
