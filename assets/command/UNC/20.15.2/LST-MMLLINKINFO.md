---
id: UNC@20.15.2@MMLCommand@LST MMLLINKINFO
type: MMLCommand
name: LST MMLLINKINFO（查询MML服务连接信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMLLINKINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- MML维护
- 连接管理
status: active
---

# LST MMLLINKINFO（查询MML服务连接信息）

## 功能

用于查询MMLService直连通道的连接信息。

## 注意事项

无

## 参数

无。

## 操作的配置对象

- [MML服务连接信息（MMLLINKINFO）](configobject/UNC/20.15.2/MMLLINKINFO.md)

## 使用实例

查询MMLService连接信息：

```
%%LST MMLLINKINFO:;%%
RETCODE = 0  操作成功  

操作结果如下 
------------ 
        连接端口号  =  9000 
        并发连接数  =  16
连接超时时间（分）  =  5
(结果个数 = 1) 
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MML服务连接信息（LST-MMLLINKINFO）_00120128.md`
