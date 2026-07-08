---
id: UDG@20.15.2@MMLCommand@DSP RVKLICINFO
type: MMLCommand
name: DSP RVKLICINFO（显示License失效信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RVKLICINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP RVKLICINFO（显示License失效信息）

## 功能

该命令用于显示License的失效信息 。

- 如果不设置“License文件名称”，则显示当前所有失效的License的信息。
- 如果设置了“License文件名称”，则显示指定License的失效信息，License文件名可以通过命令获取[LST LICENSE](查询License(LST LICENSE)_00220006.md)。

> **说明**
> 无

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FN | License文件名称 | 可选必选说明：可选参数。<br>参数含义：用于具体描述一个License文件名称。<br>取值范围：<br>长度为6~311的字符串<br>。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [License失效信息（RVKLICINFO）](configobject/UDG/20.15.2/RVKLICINFO.md)

## 使用实例

查询指定License"license_xx.xml"的失效信息：

```
%%DSP RVKLICINFO: FN="license_xx.xml";%%
RETCODE = 0  操作成功

License失效信息
---------------
License文件名称  =  license_xx.xml
  License序列号  =  LIC201908240XXXXX
  License失效码  =  LIC201908240XXXXX:0133973F96EF622101A6D2558011F7498907XXXX
       失效时间  =  2019-11-21 16:57:52
(结果个数 = 1)

---    END
```

查询所有License失效信息：

```
%%DSP RVKLICINFO:;%%
RETCODE = 0  操作成功

License失效信息
---------------
License文件名称      License序列号        License失效码                                               失效时间 

license_xx1.xml      LIC201602294XXXXX    LIC20171116012XXX:66326438736BC7FBCC0C15D9BDBA1473C610XXXX  2016-01-05 09:43:24
license_xx2.xml      LIC201602295XXXXX    LIC20171116012XXX:66326438736BC7FBCC0C15D9BDBA1473C610XXXX  2016-01-05 09:43:24
license_xx3.xml      LIC201602296XXXXX    LIC20171116012XXX:66326438736BC7FBCC0C15D9BDBA1473C610XXXX  2016-01-05 09:43:24
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示License失效信息(DSP-RVKLICINFO)_00381870.md`
