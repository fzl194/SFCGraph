---
id: UDG@20.15.2@MMLCommand@ACT LICENSE
type: MMLCommand
name: ACT LICENSE（激活License）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: LICENSE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# ACT LICENSE（激活License）

## 功能

![](激活License(ACT LICENSE)_99793370.assets/notice_3.0-zh-cn.png)

此操作将会影响网元业务，请确认将要激活的License文件是否正确，再进行此操作。

该命令用于激活License。

该命令的使用场景为：

- 在新建场景中，操作员需要使用该命令激活有效的License文件，使用户能够获得系统用户容量和功能等使用权。
- 在扩容场景中，如果用户申请了新的License控制项功能，操作员需要使用该命令激活新申请的License文件，这样用户才能获得该新功能的服务。
- 当使用中的License文件到期时，用户需要重新申请一个新的License文件，否则原有License控制的功能将无法使用，操作员需要使用该命令激活新申请的License文件，继续获得所需功能的服务。

> **说明**
> - 在执行[**ACT LICENSE**](激活License(ACT LICENSE)_99793370.md)命令之前，License文件必须通过OM Portal上传。操作步骤为：
>     1. 在菜单栏中选择“应用管理 > 应用License > License文件管理”，进入License文件管理界面。
>     2. 点击“上传License文件”按钮，在弹窗中点击“浏览”选择要上传的License文件。
>     3. 点击“确定”按钮，开始上传，上传成功后，可在列表中看到已上传的License文件。
>
> - 当系统中已经存在激活的License，再激活另一个License时，若存在控制项的值变小或控制项消失的情况，详细信息会在返回报文中体现。
> - 回退License可由该命令实现。只支持回退为系统当前存在且未失效的License文件。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| FN | License文件名称 | 可选必选说明：必选参数。<br>参数含义：用于具体描述一个License文件名称。<br>取值范围：长度为6~311的字符串。文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：<br>确认文件在License文件管理界面<br>存在。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LICENSE]] · 失效License（LICENSE）

## 使用实例

激活License文件LIC20090217003.dat：

```
%%ACT LICENSE: FN="LIC20090217003.dat";%%
RETCODE = 0  操作成功

减少的控制项
------------
当前License文件名       先前License文件名      控制项     控制项描述            当前值   先前值   当前值截止日期  先前值截止日期

LIC20090217003.dat      LIC20090226000D00.dat  basicfun3  呼叫数                4000     5000000  2020-12-05      2020-10-31  
LIC20090217003.dat      LIC20090226000D00.dat  basicres3  XX版本灵活控制功能    0        1        2020-12-05      2020-10-31     
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ACT-LICENSE.md`
