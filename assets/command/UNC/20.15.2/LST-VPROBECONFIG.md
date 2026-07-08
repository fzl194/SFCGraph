---
id: UNC@20.15.2@MMLCommand@LST VPROBECONFIG
type: MMLCommand
name: LST VPROBECONFIG（查询vProbe文件管理规格配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPROBECONFIG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe文件管理规格配置
status: active
---

# LST VPROBECONFIG（查询vProbe文件管理规格配置）

## 功能

该命令用于显示vProbe文件管理的规格配置信息。

## 注意事项

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPROBECONFIG]] · vProbe文件管理规格配置（VPROBECONFIG）

## 使用实例

运营商A查询vProbe的文件管理规格配置信息：

```
%%LST VPROBECONFIG:;%%
RETCODE = 0  操作成功

结果如下
--------
缓存文件存储空间大小(GB)  =  20
    文件最长写入时间(秒)  =  300
    文件最大写入大小(MB)  =  100
    文件最长存留时间(天)  =  7
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VPROBECONFIG.md`
