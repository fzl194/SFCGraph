---
id: UNC@20.15.2@ConfigObject@LICENSE
type: ConfigObject
name: LICENSE（失效License）
nf: UNC
version: 20.15.2
object_name: LICENSE
object_kind: action
status: active
---

# LICENSE（失效License）

## 说明

![](失效License(RVK LICENSE)_00061904.assets/notice_3.0-zh-cn_2.png)

该命令会使License失效，请确认是否要进行操作。

该命令用于使License失效，当前系统激活的License失效后，会进入宽限期阶段，失效的License不能被激活和回退。

- 如果不设置“License文件名称”，则失效当前系统激活的License，失效后会进入宽限期阶段。
- 如果设置了“License文件名称”，且不是当前系统激活的License，则只会使此License失效，不会对系统激活的License产生影响，此License不能再用于激活和回退。

该命令的使用场景为：在ESN变更、容量调整等场景下，使用本命令使License文件失效并获取失效码，用于重新获取新的License文件。

## 操作本对象的命令

- [ACT LICENSE](command/UNC/20.15.2/ACT-LICENSE.md)
- [CMP LICENSE](command/UNC/20.15.2/CMP-LICENSE.md)
- [DSP LICENSE](command/UNC/20.15.2/DSP-LICENSE.md)
- [LST LICENSE](command/UNC/20.15.2/LST-LICENSE.md)
- [RVK LICENSE](command/UNC/20.15.2/RVK-LICENSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/失效License(RVK-LICENSE)_00061904.md`
- 原始手册：`evidence/UNC/20.15.2/显示License(DSP-LICENSE)_00360098.md`
- 原始手册：`evidence/UNC/20.15.2/查询License(LST-LICENSE)_00220006.md`
- 原始手册：`evidence/UNC/20.15.2/比较License(CMP-LICENSE)_46941849.md`
- 原始手册：`evidence/UNC/20.15.2/激活License(ACT-LICENSE)_99793370.md`
