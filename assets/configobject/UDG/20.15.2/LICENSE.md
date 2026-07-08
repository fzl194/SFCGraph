---
id: UDG@20.15.2@ConfigObject@LICENSE
type: ConfigObject
name: LICENSE（失效License）
nf: UDG
version: 20.15.2
object_name: LICENSE
object_kind: action
status: active
---

# LICENSE（失效License）

## 说明

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

## 操作本对象的命令

- [[command/UDG/20.15.2/ACT-LICENSE]] · ACT LICENSE
- [[command/UDG/20.15.2/CMP-LICENSE]] · CMP LICENSE
- [[command/UDG/20.15.2/DSP-LICENSE]] · DSP LICENSE
- [[command/UDG/20.15.2/LST-LICENSE]] · LST LICENSE
- [[command/UDG/20.15.2/RVK-LICENSE]] · RVK LICENSE

## 证据

- 原始手册：`evidence/UDG/20.15.2/LICENSE.md`
- 原始手册：`evidence/UDG/20.15.2/LICENSE.md`
- 原始手册：`evidence/UDG/20.15.2/LICENSE.md`
- 原始手册：`evidence/UDG/20.15.2/LICENSE.md`
- 原始手册：`evidence/UDG/20.15.2/LICENSE.md`
