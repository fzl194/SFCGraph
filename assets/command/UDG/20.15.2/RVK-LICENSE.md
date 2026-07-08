---
id: UDG@20.15.2@MMLCommand@RVK LICENSE
type: MMLCommand
name: RVK LICENSE（失效License）
nf: UDG
version: 20.15.2
verb: RVK
object_keyword: LICENSE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# RVK LICENSE（失效License）

## 功能

![](失效License(RVK LICENSE)_00061904.assets/notice_3.0-zh-cn.png)

该命令会使License失效，请确认是否要进行操作。

该命令用于使License失效，当前系统激活的License失效后，会进入宽限期阶段，失效的License不能被激活和回退。

- 如果不设置“License文件名称”，则失效当前系统激活的License，失效后会进入宽限期阶段。
- 如果设置了“License文件名称”，且不是当前系统激活的License，则只会使此License失效，不会对系统激活的License产生影响，此License不能再用于激活和回退。

该命令的使用场景为：在ESN变更、容量调整等场景下，使用本命令使License文件失效并获取失效码，用于重新获取新的License文件。

> **说明**
> - 如果设备ESN和License文件ESN不匹配，则不允许失效。
> - 如果License文件已过期，则不允许失效。
> - 如果系统处于紧急状态，则不允许失效当前运行的License。
> - 如果License已经失效，则不允许再次失效。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FN | License<br>文件名称 | 可选必选说明：可选参数。<br>参数含义：<br>用于具体描述一个License文件名称。<br>取值范围：长度为6~311的字符串。<br>文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LICENSE]] · 失效License（LICENSE）

## 使用实例

失效License文件：

```
%%RVK LICENSE: FN="license_xx1.xml";%%
RETCODE = 0  操作成功

License失效信息
---------------
License序列号  =  LIC20190824XXXXXX
License失效码  =  LIC20190824XXXXXX:0133973F96EF622101A6D25XXXXXX
     失效时间  =  2019-11-21 16:57:52
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RVK-LICENSE.md`
