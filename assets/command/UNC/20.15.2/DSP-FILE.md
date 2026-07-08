---
id: UNC@20.15.2@MMLCommand@DSP FILE
type: MMLCommand
name: DSP FILE（查询文件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FILE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 文件传输
status: active
---

# DSP FILE（查询文件信息）

## 功能

用于从数据库中查询出当前系统中的一级目录信息，以及呈现出指定目录下磁盘和数据库中的不一致的文件信息。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 场景 | 可选必选参数说明：必选参数。<br>参数含义：用于请求系统查询目录概要或查询指定目录下不一致文件信息。<br>取值范围：<br>- “DIRSUMMARY(目录概要)”：用于显示系统中一级目录信息。<br>- “INCONSISTENTFILE(不一致文件)”：用于显示系统中指定目录下磁盘和数据库中的不一致的文件信息。<br>默认值：无。<br>配置原则：无。 |
| DIRID | 目录ID | 可选必选参数说明：该参数在<br>“场景”<br>配置为<br>“INCONSISTENTFILE(不一致文件)”<br>时为条件必选参数。<br>参数含义：用于表示目录ID。<br>取值范围：0～2147483647。<br>默认值：无。<br>配置原则：<br>“场景”<br>参数配置为<br>“DIRSUMMARY(目录概要)”<br>时可查询<br>“目录ID”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILE]] · 文件传输（FILE）

## 使用实例

查询一级目录概要：

```
%%DSP FILE: SCENE=DIRSUMMARY;%%
RETCODE = 0  操作成功

FileServer基本信息
------------------
服务实例  状态  根目录数

10.0.0.1  正常  2
10.0.0.2  正常  2
(结果个数 = 2)

目录信息
--------
目录ID  目录名称  目录权限  单个文件大小上限（KB）  文件个数上限  目录大小上限（MB）  允许文件类型                                 是否备份  

1       系统文件  只读      2097152                 100           4096.00             xml,yaml,json,txt,tar.gz,gz,tar,zip,ini,sql  是        
2       应用文件  读写      307200                  100           4096.00             xml,yaml,json,txt,tar.gz,gz,tar,zip,ini,sql  是               
(结果个数 = 2)

---    END
```

查询指定目录下不一致文件信息：

```
%%DSP FILE: SCENE=INCONSISTENTFILE, DIRID=2;%%
RETCODE = 0  操作成功

FileServer基本信息
------------------
服务实例  状态  根目录数

10.0.0.1  正常  2
10.0.0.2  正常  2
(结果个数 = 2)

不一致数据
----------
文件名       归属根目录           文件归类  服务实例  不一致原因                        

1/test8.txt  /2_Application file  文件      10.0.0.2  冗余  
100.txt      /2_Application file  文件      10.0.0.2  缺失
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FILE.md`
