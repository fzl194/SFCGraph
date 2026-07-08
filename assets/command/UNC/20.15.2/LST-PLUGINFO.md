---
id: UNC@20.15.2@MMLCommand@LST PLUGINFO
type: MMLCommand
name: LST PLUGINFO（查询插件信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLUGINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 应用管理
status: active
---

# LST PLUGINFO（查询插件信息）

## 功能

本命令用于支持网元查询已安装的插件列表和插件版本号。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPID | 网元ID | 可选必选说明：可选参数。<br>参数含义：用于指示系统按照网元ID来查询插件信息；若不输入则查询所有的插件信息。<br>取值范围：0~1024<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLUGINFO]] · 插件信息（PLUGINFO）

## 使用实例

查询 UNC 网元已安装的插件列表：

```
%%LST PLUGINFO:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
      网元ID  =  0
    插件类型  =  CONFIG
    插件包名  =  
UNC
_22.1.0.1_PLUGIN_CONFIG_X86.zip
    插件版本  =  
UNC
_22.1.0.1
插件安装状态  =  已安装
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询插件信息(LST-PLUGINFO)_99748749.md`
